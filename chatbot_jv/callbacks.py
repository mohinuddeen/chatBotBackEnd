"""
Chatbot Callbackes registration
"""
import warnings
import wikipedia
from chatbot import register_call


warnings.filterwarnings("ignore")


@register_call("whoIs")
def get_info(session, query):
    """
    Get information about a person or object on Wikipedia
    Args:
        session (Session): Session object to retrieve
        query (str): User query

    Returns:
        str : Response string
    """
    try:
        return wikipedia.summary(query)
    except Exception:
        pass
    for new_query in wikipedia.search(query):
        try:
            return wikipedia.summary(new_query)
        except Exception:
            pass
    return "I don't know about " + query
