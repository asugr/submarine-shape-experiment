import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Submarine Shape Lab", page_icon="🌊", layout="wide")
st.title("🌊 Why Are Submarines Shaped Like Cigars?")
st.caption("Educational fluid-dynamics experiment — simplified model, not a real submarine design tool.")

rho=st.slider("Water density (kg/m³)",1000,1035,1025)
speed=st.slider("Speed (m/s)",1.0,20.0,10.0,0.5)
area=st.slider("Reference frontal area (m²)",4.0,20.0,12.0,0.5)

shapes={"Sphere":0.47,"Blunt cylinder":1.05,"Streamlined teardrop":0.12}
shape=st.selectbox("Conceptual body",list(shapes))
cd=shapes[shape]
drag=0.5*rho*speed**2*cd*area
power=drag*speed

c1,c2,c3=st.columns(3)
c1.metric("Estimated drag",f"{drag:,.0f} N")
c2.metric("Idealized drag power",f"{power/1000:,.1f} kW")
c3.metric("Drag coefficient",f"{cd:.2f}")

st.divider()
st.markdown("### Compare the three conceptual shapes")
data=[(n,0.5*rho*speed**2*c*area) for n,c in shapes.items()]
fig,ax=plt.subplots(figsize=(8,4.5))
ax.bar([x[0] for x in data],[x[1] for x in data])
ax.set_ylabel("Estimated drag (N)")
ax.set_title(f"Drag at {speed:.1f} m/s")
st.pyplot(fig)

st.info("The drag coefficients are illustrative values for a conceptual comparison. Real submarine drag depends on Reynolds number, hull geometry, appendages, surface roughness, flow regime and other factors.")
