def simple_chatbot():
    print("សួស្ដី! ខ្ញុំជា Chatbot របស់អ្នក។ តើខ្ញុំអាចជួយអ្វីអ្នកបាន?")
    print("អ្នកអាចវាយ 'ចេញ' ដើម្បីបញ្ចប់ការសន្ននា។")

    while True:
        user_input = input("អ្នក: ").lower()

        if user_input == "ចេញ":
            print("Chatbot: លាហើយ! ឈប់និយាយរកហើយ។")
            break
        elif "សួស្ដី" in user_input:
            print("Chatbot: សួស្ដី! តើអ្នកសុខសប្បាយជាទេ?")
        elif "សុខសប្បាយ" in user_input:
            print("Chatbot: ល្អណាស់! តើអ្នកមានអ្វីចង់សួរខ្ញុំទេ?")
        elif "ឈ្មោះ" in user_input:
            print("Chatbot: ខ្ញុំគ្មានឈ្មោះទេ។ I'm just a Chatbot!")
        elif "អាយុ" in user_input:
            print("Chatbot: ខ្ញុំជាកម្មវិធីកំព្យូទ័រ ដូច្នេះខ្ញុំគ្មានអាយុទេ។")
        elif "អគុណ" in user_input:
            print("Chatbot: រីករាយណាស់ដែលបានជួយ។")
        elif "អាកាសធាតុ" in user_input:
            print("Chatbot: ខ្ញុំមិនអាចមើលឃើញព័ត៍មានអាកាសធាតុបច្ចុប្បន្នទេ។")
        elif "ជំនួយ" in user_input:
            print("Chatbot: ខ្ញុំមិនចេះអ្វីទេ។")
        elif "ស្នេហា" in user_input:
            print("Chatbot: បងស្រឡាញ់អូន!")
        elif "បែកគ្នាទៅ" in user_input:
            print("Chatbot: ទៅៗ អូនសម្លាញ់ :P")
        else:
            print("Chatbot: ខ្ញុំមិនយល់សំណួររបស់អ្នកទេ។ សូមសាកល្បងម្ដងទៀត។")

# Run Chatbot
if __name__ == "__main__":
    simple_chatbot()
