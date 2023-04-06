import assistant_details
from database import speak_is_on
from speak_module import speak

def output(o):
    
    # command line output
    
    if speak_is_on():
        speak(o)
        
        
    print(assistant_details.name+ ":" + o)
    print()