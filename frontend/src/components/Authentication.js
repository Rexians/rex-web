import { Navigate } from "react-router-dom";
import { useEffect } from "react";
import { auth } from "../api/Auth";

const Authentication = ({ setLogged }) => {
  // Function to check if user is logged in. Set local storage based on that
  // setLogged state to true or false if logged in or not. This will help re render the site
  const isAuth = async function () {
    const logged = (await auth())["logged"];
    if (logged) {
      window.localStorage.setItem("logged", "true");
      setLogged(true);
    } else {
      window.localStorage.setItem("logged", "false");
      setLogged(false);
    }
  };

  useEffect(() => {
    isAuth();
  }, []);

  return <Navigate to="/home" />;
};

export default Authentication;
