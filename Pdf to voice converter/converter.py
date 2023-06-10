import PyPDF2 as pdf 
import pyttsx3 as tx


def pdf_to_mb3():
    file=input("inter the path of the file u want to convert to mp3:\n")
    pdf_reader=pdf.PdfReader(open(str(file),'rb'))
    speaker=tx.init()
    #print(len(pdf_reader.pages))
    final_text=""
    for page in range(len(pdf_reader.pages)):
        text=pdf_reader.pages[page].extract_text()
        clean_text=text.strip().replace('\n', '    ')
        #clean_text=text.strip().replace(' ', '  ')
        final_text += clean_text
        print(final_text)
    
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-55)

    file_save_path= input('where do u want to save the file (inter vaild path:)\n')
    file_name=input ('what is the name u want to call the file with: \n')
    speaker.save_to_file(final_text,str(file_save_path)+'\\' +str(file_name)+ '.mp3' ) 
    speaker.runAndWait()
    speaker.stop()
    
pdf_to_mb3()