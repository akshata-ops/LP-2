import random
def get_bot_response(user_input):
    responses = {
        "hi":"hello!,How can I assit you?",
        "how are you?":"I am just computer program,thanks for asking",
        "default":"I'am unable to understand can you plz rephrase.",
        "which are the top most colleges for engineering in pune?": ["COEP", "PICT", "PCCOE", "CUMMINS", "VIT"],
        "which are the top most engineering branches?": ["Computer Engineering", "IT Engineering", "Entc Engineering"],
        "what is the cut-off for top most branches in coep?": ["Computer Engineering: 99.90 percentile", "IT Engineering is not provided", "EnTC Engineering: 97.90 percentile"],
        "what is the cut-off for top most branches in pict?": ["Computer Engineering: 98.90 percentile", "IT Engineering: 97.90 percentile", "EnTC: 95.90 percentile"],
        "what is the cut-off for top most branches in pccoe?": ["Computer Engineering: 97.90 percentile", "IT Engineering: 96.90 percentile", "EnTC Engineering: 94.90 percentile"],
        "what is the cut-off for top most branches in cummins?": ["Computer Engineering: 98.90 percentile", "IT Engineering:95.90 percentile", "EnTC Engineering: 93.90 percentile"],
        "what is the cut-off for top most branches in vit?": ["Computer Engineering: 95.90 percentile", "IT Engineering: 93.90 percentile", "EnTC Engineering: 90.90 percentile"],
        "when will admission process start?": "In last month of June"
    }
    return responses.get(user_input.lower(), responses["default"])
    print(" ")
def main():
    print("This is simple chatbot for college inquriy")
    print(" ")
    while True:
        user_input=input("You:")
        if user_input.lower()=='bye':
            print("Bot:goodbye!,assit you soon!")
            break
        bot_response=get_bot_response(user_input)
        print("Bot:",bot_response)


if __name__=="__main__":
    main()
