import main as st
import openai

# API anahtarını ayarlayın
openai.api_key = st.secrets["OPENAI_API_KEY"]


def generate_campaign_text(target_audience, campaign_topic, word_count, emoji_usage, kampanya_sayısı):
    emoji_prompt = "kullanılsın" if emoji_usage == "Kullanılsın" else "kullanılmasın"
    prompt = f"{target_audience} hedef kitlesine yönelik, {campaign_topic} konusunu merkeze alan {word_count} karakter sayısına ve harekete geçirici sloganlara ve {target_audience} kitlesine uygun bir dile sahip {kampanya_sayısı} tane farklı kampanya metni yazın. Bu kampanyada emojiler {emoji_prompt}."
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return output['choices'][0]['message']['content']

def main():
    st.title("Kampanya Metni Oluşturucu")
    st.write("Bu uygulama, hedef kitle, kampanya konusu ve kelime sayısı temelinde bir kampanya metni oluşturur.")

    target_audience = st.text_input("Hedef kitlenizi girin:")
    campaign_topic = st.text_input("Kampanya konusunu girin:")
    word_count = st.number_input("İstenen karakter sayısını girin:", min_value=0, max_value=500, step=1, value=200)
    emoji_usage = st.selectbox("Emojileri Kullanımı:", options=["Kullanılsın", "Kullanılmasın"])
    kampanya_sayısı = st.number_input("Üretilmesini istediğiniz kampanya metni sayısını girin:", min_value=0, max_value=10, step=1, value=2)
    
    if st.button("Kampanya Metnini Oluştur"):
        if target_audience or campaign_topic :
            campaign_text = generate_campaign_text(target_audience, campaign_topic, word_count, emoji_usage, kampanya_sayısı)
            st.write(campaign_text)
    if st.button("Tekrar Dene"):
        if target_audience or campaign_topic :
            campaign_text = generate_campaign_text(target_audience, campaign_topic, word_count, emoji_usage, kampanya_sayısı)
            st.write(campaign_text)

if __name__ == "__main__":
    main()