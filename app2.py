import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "About us",
        "Team",
        "Buy Fortunes",
        "Stake Fortunes",
        "Roadmap",
        "Newsletter",
        "Analytics",
    ]
)

with tab1:
    st.header("Defi Don")
    st.markdown(
        """
        Empowering Cryptocurrency with Fortunes

Defi Don stands as a decentralized cryptocurrency platform, underpinned by the "Fortunes" coin. Our mission revolves around creating a versatile coin designed for trading, holding, and staking. We place paramount importance on executing our objectives with unwavering integrity and fostering transparent relationships with our valued investors.

Outlined below are key facets encapsulating our vision:

1. **Decentralized Coin**: We are committed to the ideology of decentralization, ensuring that the Fortunes coin remains free from the control of any singular entity.

2. **Performance-Tied Token**: The Fortunes coin is intrinsically linked to the performance of our exclusive trading bot, known as "Pindabot". This linkage translates into investor rewards that dynamically adjust based on the bot's efficacy.

3. **Utility in E-Commerce**: The Fortunes coin doubles as a means to purchase goods and services on our web-based platform, amplifying its utility and integration within the broader digital ecosystem.

4. **Democratic Decision-Making**: Our coin also serves as a tool for democratic participation. Investors can wield their Fortunes tokens to influence pivotal decisions concerning the platform's development trajectory.

At Defi Don, we're not just crafting a cryptocurrency; we're architecting a resilient financial instrument with a multifaceted purpose. Our commitment to transparency, decentralization, and innovation propels us toward a future where the Fortunes coin becomes an embodiment of empowerment and inclusion.
            """
    )

with tab2:
    st.header("Don Fortunes Team")
    st.markdown(
        """
        Pinda Johnson \n
        Dylan Brown \n
        Branzil Engracia \n
            
        We proudly represent a vibrant and multifaceted collective comprising individuals who are not only 
        ardent aficionados of technology and blockchain but also visionary entrepreneurs. 
        Our unified mission revolves around the provision of an unparalleled blend of convenience and 
        profitability within the realm of digital currency investment, catering to a broad spectrum of investors. 
        Through our unwavering dedication, extensive expertise, and fervent passion for cutting-edge advancements, 
        we strive to usher in a new era of financial empowerment, ensuring that every investor, regardless of background or 
        experience, can seamlessly partake in the transformative potential of digital currencies.
    """
    )
    st.image("coin_logo.png", width=500)

with tab3:
    st.header("Buy Fortunes")
    st.text_input("Enter your wallet address")
    st.number_input("How much Fortunes Do you want to purchase?")

with tab4:
    st.header("Stake Fortunes")
    st.number_input("How much Fortunes Do you want to Stake with us?")
    st.write(
        """At DeFi Don, we pride ourselves on utilizing a unique and proprietary trading strategy
             that has been carefully crafted and refined over time. Our advanced trading bot, 
             which is the result of extensive research and development, 
             is engineered to maximize profitability. 
             This bot continuously scans and trades across multiple markets, 
             ensuring that we take advantage of the best opportunities throughout the entire year. 
             Our commitment to this approach allows us to consistently stay ahead in the dynamic world of 
             decentralized finance, delivering optimal returns for our stakeholders"""
    )


with tab5:
    st.header("Roadmap")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab6:
    st.header("Newsletter")
    st.text_input("Enter your email address below for updates!!!")

with tab7:
    st.header("Analytics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Price", "$20356", "$19655")
    col2.metric("Market Cap", "$508,797", "$508,766")
    col3.metric("Volume", "$12,804", "$12,809")
    col4.metric("Circulating Supply", "19,523")
