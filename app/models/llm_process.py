from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
import pandas as pd
from transformers import pipeline
import pandas as pd
import ollama

def sentiment_analysis(df:pd.DataFrame):

    if not os.path.exists('./sentiment_model'):
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"

        print("Downloading model and tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)

        local_path = "./sentiment_model"
        tokenizer.save_pretrained(local_path)
        model.save_pretrained(local_path)

        print(f"Successfully downloaded and saved to: {local_path}")

    
    local_path = "./sentiment_model"


    print("Loading sentiment analysis model from local drive...")
    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model=local_path, 
        tokenizer=local_path,
        truncation=True 
    )

    df['sentiment']=[result['label'] for result in sentiment_pipeline(df['Comment'].to_list())]

    """mapping_dict = {
    'POSITIVE': 1,
    'NEGATIVE': 0
    }

    df['sentiment_numeric'] = df['sentiment'].map(mapping_dict)
    """
    
    return df




def llm_result(df:pd.DataFrame):

    negative_df = df[df['sentiment'] == 'NEGATIVE']
    positive_df = df[df['sentiment'] == 'POSITIVE']

    negative_comments = negative_df['Comment'].tolist()
    positive_comments = positive_df['Comment'].tolist() 

    Neg_comments_text = "\n- ".join(negative_comments[:150])
    pos_comment_test = "\n-".join(positive_comments[:150])

    num_positive = (df['sentiment'] == 'POSITIVE').sum()
    num_negative = (df['sentiment'] == 'NEGATIVE').sum()

    prompt = f"""
    You are an expert data analyst. I am going to give you a list of negative and postive YouTube comments.
    Please read through them and give me a summary of the positive and negative comments i will also tell you what is the sentiment of top 500 comments this is just for your context 
    and you should not tell how many comments are positive or negative you can use words like most , some , etc to describe the sentiments of the comments.
    give a brief summary.

    Here are the comments:
    - negative comments - {Neg_comments_text}
    - positve comments - {pos_comment_test}

    and the sentiment of top 500 comment are - [positive = {num_positive}] ,[negative={num_negative}]
    """


    print("Thinking... (this might take a moment depending on your computer's speed)")

    response = ollama.chat(
        model='llama3.2', 
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )


    print("\n--- LLAMA 3.2 ANALYSIS ---")
    respo = response['message']['content']
    return respo