### Erste Streamlit App

import streamlit as st
from queries import find_devices
from devices import Device

# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")

# tabs
tab1, tab2, tab3 = st.tabs(["Gerät anlegen", "Geräte Verwalten","Gerät reservieren"])


with tab1:
    with st.form("New Device"):
            

            #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
            #loaded_device.is_active = checkbox_val

            new_devicename = st.text_input("Gerätename")
            device_user = st.text_input("Verantwortlicher")
            

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_device= Device(new_devicename,device_user)
                new_device.store_data()
                st.write("Data stored.")
                st.rerun()

    


with tab2:

    genre = st.radio("Bitte auswählen",
    ["Verantwortlichen ändern", "Gerät löschen"],
    captions = ["", ""])

    if genre == "Verantwortlichen ändern":

        # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
        devices_in_db = find_devices()

        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice")

            if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                st.write(f"Loaded Device: {loaded_device}")


            with st.form("Device"):
                st.write(loaded_device.device_name)

                #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
                #loaded_device.is_active = checkbox_val

                text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
                loaded_device.managed_by_user_id = text_input_val

                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")
                if submitted:
                    loaded_device.store_data()
                    st.write("Data stored.")
                    st.rerun()
    
    elif genre == "Gerät löschen":
        
        devices_in_db = find_devices()
        if devices_in_db:
            current_device_name = st.selectbox(
                'Gerät auswählen',
                options = devices_in_db, key="sbDevice")

            if current_device_name in devices_in_db:
                loaded_device = Device.load_data_by_device_name(current_device_name)
                st.write(f"Loaded Device: {loaded_device}")


            with st.form("Device"):
                st.write(loaded_device.device_name,"wirklich löschen?")

                

                #hier löschen implementieren


                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")  #macht momentan nichts
                if submitted:
                    loaded_device.store_data()
                    st.write("Data stored.")
                    st.rerun()
    
with tab3:
     # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
    devices_in_db = find_devices()

    if devices_in_db:
        current_device_name = st.selectbox(
            'Gerät auswählen',
            options = devices_in_db, key="sbDevice_reservation")

        if current_device_name in devices_in_db:
            loaded_device = Device.load_data_by_device_name(current_device_name)
            st.write(f"Loaded Device: {loaded_device}")


        with st.form("Device reservation"):
            st.write(loaded_device.device_name)

            #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
            #loaded_device.is_active = checkbox_val

            reservieren_time = st.text_input("reservation time")
            reservation_devicename = loaded_device.device_name
            

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_reservation = reservation.reservation(reservieren_time, reservation_devicename)
                loaded_device.store_data()
                st.write("Data stored.")
                st.rerun()