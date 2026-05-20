from app.models.commets_retrive import get_comments
from app.models.llm_process import sentiment_analysis,llm_result

def run_analysis(vid_id):

    df= get_comments(vid_id)
    df= sentiment_analysis(df)
    result=llm_result(df)
    print(result)
    return result
