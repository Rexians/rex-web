import { Navigate } from "react-router-dom";
import { auth } from "../api/Auth";
import { useEffect } from "react";
import React from "react";

const Authentication = () => {
  const isAuth = async function () {
    const logged = (await auth())["logged"];
    console.log(logged);
    if (logged) {
      window.localStorage.setItem("logged", "true");
    } else {
      window.localStorage.setItem("logged", "false");
    }
  };

  useEffect(() => {
    isAuth();
  }, []);

  return <Navigate to="/home" />;
};

export default Authentication;
