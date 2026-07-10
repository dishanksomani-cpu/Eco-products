import streamlit as st

st.set_page_config(
    page_title="EcoCycle Marketplace",
    page_icon="♻️",
    layout="wide"
)

# ------------------------
# Custom CSS
# ------------------------

st.markdown("""
<style>

.main {
    background-color:#f6fff8;
}

h1,h2,h3{
    color:#0d6832;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.metric{
    background:#eafaf1;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

button[kind="primary"]{
    background:#198754;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# Title
# ------------------------

st.title("♻️ EcoCycle Marketplace")

st.subheader("Turning Plastic Waste into Sustainable Products")

st.write(
"""
Welcome to **EcoCycle Marketplace**, where plastic waste is transformed into
high-quality sustainable products.

Our mission is to reduce landfill waste while promoting a circular economy.
"""
)

st.divider()

# ------------------------
# Dashboard
# ------------------------

st.header("📊 Sustainability Dashboard")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Plastic Recycled","12,450 kg","+350 kg")

with c2:
    st.metric("Products Sold","3,270","+90")

with c3:
    st.metric("CO₂ Saved","28 Tons","+1.4 Tons")

with c4:
    st.metric("Customers","1,150","+42")

st.divider()

# ------------------------
# Products
# ------------------------

products=[
{
"name":"Recycled Plastic Chair",
"category":"Furniture",
"price":45,
"rating":4.8,
"material":"100% Recycled Plastic",
"description":"Durable eco-friendly chair made from recycled plastic."
},

{
"name":"Eco Plant Pot",
"category":"Gardening",
"price":15,
"rating":4.7,
"material":"Recycled Plastic",
"description":"Beautiful plant pot suitable for indoor and outdoor use."
},

{
"name":"Recycled Storage Box",
"category":"Home",
"price":22,
"rating":4.9,
"material":"Plastic Waste",
"description":"Strong storage box made entirely from recycled plastic."
},

{
"name":"Eco Table",
"category":"Furniture",
"price":120,
"rating":4.6,
"material":"Industrial Plastic Waste",
"description":"Stylish table built from industrial plastic waste."
},

{
"name":"Reusable Water Bottle",
"category":"Lifestyle",
"price":18,
"rating":4.9,
"material":"Food Grade Recycled Plastic",
"description":"Reusable bottle promoting sustainable living."
},

{
"name":"Outdoor Bench",
"category":"Furniture",
"price":210,
"rating":4.8,
"material":"Ocean Plastic",
"description":"Weather-resistant recycled outdoor bench."
}

]

st.header("🛒 Product Marketplace")

search=st.text_input("Search Product")

category=st.selectbox(
"Category",
["All"]+sorted(list(set([i["category"] for i in products])))
)

filtered=[]

for p in products:

    if search.lower() not in p["name"].lower():
        continue

    if category!="All" and p["category"]!=category:
        continue

    filtered.append(p)

if "cart" not in st.session_state:
    st.session_state.cart=[]

cols=st.columns(3)

for i,p in enumerate(filtered):

    with cols[i%3]:

        st.markdown(f"""
<div class="card">

<h3>{p['name']}</h3>

<b>Category:</b> {p['category']}<br>

<b>Material:</b> {p['material']}<br>

<b>Rating:</b> ⭐ {p['rating']}<br><br>

{p['description']}

<h2 style='color:green;'>${p['price']}</h2>

</div>
""",unsafe_allow_html=True)

        if st.button(f"Add to Cart - {p['name']}"):
            st.session_state.cart.append(p)

st.divider()

# ------------------------
# Cart
# ------------------------

st.header("🛍 Shopping Cart")

if len(st.session_state.cart)==0:

    st.info("Cart is Empty.")

else:

    total=0

    for item in st.session_state.cart:

        st.write(f"✅ {item['name']} — ${item['price']}")
        total+=item["price"]

    st.success(f"Total = ${total}")

    if st.button("Checkout"):

        st.balloons()

        st.success("Order Placed Successfully!")

        st.session_state.cart=[]

st.divider()

# ------------------------
# Why Choose Us
# ------------------------

st.header("🌍 Why EcoCycle?")

left,right=st.columns(2)

with left:

    st.markdown("""
### 🌱 Sustainability

- Reduce Plastic Pollution

- Circular Economy

- Lower Carbon Footprint

- High Quality Products

- Affordable Pricing

""")

with right:

    st.markdown("""
### 💚 Environmental Impact

✔ Ocean Plastic Recovery

✔ Zero Waste Manufacturing

✔ Renewable Energy Usage

✔ Sustainable Packaging

✔ Community Recycling Programs

""")

st.divider()

# ------------------------
# Contact
# ------------------------

st.header("📞 Contact Us")

name=st.text_input("Your Name")

email=st.text_input("Email")

message=st.text_area("Message")

if st.button("Send Message"):

    st.success("Thank you! We'll contact you soon.")

st.divider()

st.markdown("""
<div class="footer">

© 2026 EcoCycle Marketplace

Building a Cleaner Planet Through Recycling ♻️

</div>
""",unsafe_allow_html=True)
