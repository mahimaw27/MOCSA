import streamlit as st
import json
import requests
import base64
from PIL import Image
import io

def get_prediction(image_data):
  #replace your image classification ai service URL
  #change the url as yours
  url = 'https://askai.aiclub.world/748b2e83-1c0b-4dc6-b114-6356ad0b295e'
  r = requests.post(url, data=image_data)
  st.write(r)
  response = r.json()['predicted_label']
  score = r.json()['score']
  #print("Predicted_label: {} and confidence_score: {}".format(response,score))
  return response, score

#Title of the web app
st.title("MOCSA")

#header
st.header("Mobile Oral Cancer Screening Application")

#write
st.write("This web app was designed to detect whether an oral lesion is benign or malignant from images of the mouth taken my a mobile camera.")

#image reading
st.image("CAC App Final Cover Photo (800x600)- resized.png")

st.header("Instructions: 🦷")
st.write("1. Read through the information about oral cancer") 
st.write("2. Scroll down to the Image Upload section") 
st.write("3. Click on the 'Browse files' button") 
st.write("4. Upload the image you took with your device")
st.write("5. Wait for the AI to run (usually takes a few seconds)") 
st.write("6. Review your results (Benign or Malignant)")
st.write("7. Look at the next steps and resources sections")

st.subheader("Benign Oral Cancer")
st.write("Many types of benign tumors and tumor-like changes can start in the mouth or throat, such as these:")
st.write("• Peripheral giant cell granuloma")
st.write("• Fibroma") 
st.write("• Granular cell tumor") 
st.write("• Schwannoma") 
st.write("• Neurofibroma")
st.write("• Pyogenic granuloma")
st.write("• Oral hemangioma") 
st.write("These non-cancer tumors start from different kinds of cells and have many causes. Some of them may cause problems, but they're not likely to be life-threatening. The usual treatment for these types of tumors is surgery to remove them completely since they are unlikely to recur (come back).") 
st.write("-American Cancer Society")
st.image("1.jpg", caption = "Here is an example of a benign oral tumor.")
   
st.subheader("Malignant Oral Cancer")
st.write("• Almost all of the cancers in the oral cavity and oropharynx are **squamous cell carcinomas**, also called squamous cell cancers. These cancers start in squamous cells, which are flat, thin cells that form the lining of the mouth and throat.")
st.write("• **Verrucous carcinoma** is a rare type of squamous cell cancer that is most often found in the gums and cheeks. It's a low-grade (slow growing) cancer that hardly ever spreads to other parts of the body.") 
st.write("• **Minor salivary gland cancers** can start in the glands in the lining of the mouth and throat. There are many types of minor salivary gland cancers, including adenoid cystic carcinoma, mucoepidermoid carcinoma, and polymorphous low-grade adenocarcinoma.")
st.write("Leukoplakia and erythroplakia are terms used to describe certain types of tissue changes that can be seen in the mouth or throat:") 
st.write("• **Leukoplakia** is a white or gray area that does not come off when scraped.") 
st.write("• **Erythroplakia** is a flat or slightly raised, red area that often bleeds easily if it's scraped.") 
st.write("• **Erythroleukoplakia** is a patch with both red and white areas.")  
st.write("These three may be signs of cancer, they might be a pre-cancer condition called dysplasia, or they could be a harmless change.")
st.write("-American Cancer Society")
st.image("5.jpg", caption = "Here is an example of a malignant oral tumor.")

st.header("Oral Cancer Risk Factors:")
st.write("• Tobacco use of any kind, including cigarettes, cigars, pipes, and chewing tobacco") 
st.write("• Heavy alcohol use") 
st.write("• Excessive sun exposure to your lips")
st.write("• Human Papillomavirus (HPV)") 
st.write("• A weakened immune system")
st.write("• A sharp/jagged tooth, which irritates the tissue")

st.subheader("Note: The accuracy of this AI is 97.7974, meaning it will not be accurate all of the time. Please talk to your dentist about your concerns.")

st.header("Upload your Image here:")

#file uploader
image = st.file_uploader(label = "Please Upload a file", accept_multiple_files = False, help = "This will classify your image into either Benign or Malignant.")

if image:
    #converting the image to bytes
    img = Image.open(image)
    buf = io.BytesIO()
    img.save(buf,format = 'JPEG')
    byte_im = buf.getvalue()

    #converting bytes to b64encoding
    payload = base64.b64encode(byte_im)

    #setting up the image
    st.image(img)

    #predictions
    response, scores = get_prediction(payload)

    st.header("Here are the results:")
    st.subheader(response)

    st.header("Next steps:")
    st.write("If you think you have any type of oral cancer, talk to your dentist or doctor. They will do a physical examination, ask about your symptoms and might take a biopsy (take a piece of tissue for testing). Early detection can boost your chance of survival from 50% to 90%. The 5-year survival rate for those with localized disease (hasn't spread) at diagnosis is 85%, compared with only 40% in patients whose cancer has metastasized (spread) [CDC]. You should report any symptoms to your practice provider if they do not get better after 3 weeks.")
    
    st.header("Resources:")
    st.write("• Find out more information at: https://www.mouthhealthy.org/en/az-topics/o/oral-cancer?source=EBDsite") 
    st.write("• Information and helpful tips: https://www.nidcr.nih.gov/health-info/oral-cancer")
    st.write("• More about oral cancer screening: https://www.mayoclinic.org/tests-procedures/oral-cancer-screening/about/pac-20394802") 
    st.write("• How you can prevent oral cancer: https://jada.ada.org/action/showFullTableHTML?isHtml=true&tableId=undtbl1&pii=S0002-8177%2817%2930656-6")
   
