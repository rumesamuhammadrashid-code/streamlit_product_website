import streamlit as st
import urllib.parse

Whatsapp_Number = "+923220389502"

st.set_page_config(
    page_title = "TechCart",
    page_icon ="🛒",
    layout = "wide" 
)

st.title("💻 TechCart")
st.write("Smart Products.Simple Shopping.")

menu = st.radio("Menu",
               ["Home", "Product", "Categories", "About", "Contact"],
                horizontal = True
                )

st.divider()

if menu == "Home":

    st.header("Welcome to TechCart")
    
    st.subheader("Smart Products. Simple Shopping.")
    
    st.write("Discover useful and affordable technology products for your everyday needs.")

    st.button("🛍️ Shop Now")

    st.divider()

    st.header("Why Shop With Us?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("✅ Quality Products")
        st.write("We offer reliable and useful products.")

    with col2:
        st.subheader("💰 Affordable Prices")
        st.write("Get great products at reasonable prices.")

    with col3:
        st.subheader("🚚 Easy Ordering")
        st.write("Order your favorite products easily.")
    
elif menu == "Product":
    st.header("Product")
    st.write("Product will appear here")
    st.divider()
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        st.image("earbuds.png", use_container_width = True)
        st.subheader("Premium Earbuds")
        st.write("Wireless Earbuds")
        st.write("Price: Rs.4000")
        
        message = """Hello! I am Intered in ordering:
        Product: Wireless Earbuds
        Price: Rs.4000
        Please provide more details."""
        
        whatsapp_url=f"https://wa.me{Whatsapp_Number}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)
                                
    with col2:
        st.image("laptop.png", use_container_width = True)
        st.subheader("Laptop")
        st.write("8th Generation Laptop")
        st.write("Price: Rs.50000")
        
        message = """Hello! I am Intered in ordering:
        Product: Laptop
        Price: Rs.50000
        Please provide more details."""
        
        whatsapp_url=f"https://wa.me{Whatsapp_Number}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)
                
    with col3:
        st.image("mouse.png", use_container_width = True)
        st.subheader("Mouse")
        st.write("Wireless Laptop Mouse")
        st.write("Price: Rs.5000")
        
        message = """Hello! I am Intered in ordering:
        Product: Wireless Laptop Mouse
        Price: Rs.5000 
        Please provide more details."""
        
        whatsapp_url=f"https://wa.me{Whatsapp_Number}?text={urllib.parse.quote(message)}"
        
        st.link_button("🛍️ Shop Now",whatsapp_url)
                
                        
elif menu == "Categories":
    st.header("Product categories")
    st.write("Product categories will appear here")
elif menu == "About":
    st.header("About TechCart")
    st.write("Learn more about aur store")
elif menu == "Contact":
    st.header("Contact us")
    st.write("Our Contact will appear here")
else:
    st.error("Page not found")
    st.write("Please select a valid option from the menu.")