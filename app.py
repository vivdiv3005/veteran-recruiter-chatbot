import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Veteran Recruiter Assistant", layout="wide")

st.title("Veteran Talent Intelligence Assistant")

st.markdown("""
Welcome Recruiters!  
Discover high-potential Armed Forces veterans transitioning into corporate careers.
""")

# Read secrets securely
APP_ID = st.secrets["COMETCHAT_APP_ID"]
REGION = st.secrets["COMETCHAT_REGION"]
AUTH_KEY = st.secrets["COMETCHAT_AUTH_KEY"]
WIDGET_ID = st.secrets["COMETCHAT_WIDGET_ID"]

html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <script defer src="https://widget-js.cometchat.io/v3/cometchatwidget.js"></script>
</head>
<body>
<div id="cometchat"></div>

<script>
window.addEventListener('DOMContentLoaded', (event) => {{

  CometChatWidget.init({{
    "appID": "1678722f7912193e5",
    "appRegion": "IN",
    "authKey": "1109c27e9026b41f371b82fec3cc50968fa81b4e"
  }}).then(response => {{

    CometChatWidget.login({{
      uid: "recruiter1"
    }}).then(response => {{

      CometChatWidget.launch({{
        widgetID: "6a0192ad130bd98e16457f81",
        target: "#cometchat",
        roundedCorners: "true",
        height: "700px",
        width: "100%"
      }});

    }});

  }});

}});
</script>
</body>
</html>
"""

components.html(html_code, height=750)
