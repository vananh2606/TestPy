def output_message():
    print("Hey this is working ... cool!")
def welcome_by_name(name):
    print("Hi there {}. Good to meet you.".format(name))
def multiply():
    user_input = int(input("Please provide a number. We will multiply it by 100: "))
    final_num = user_input * 100
    print("Your number is: {}".format(final_num))