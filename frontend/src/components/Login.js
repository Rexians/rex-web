import Navigation from "./Navigation";
import "../styles/Login.css";

const Login = () => {
  return (
    <div>
      <Navigation />
      <div className="loginform">
        <div className="loginheader"></div>
        <button className="loginbutton">Login through Discord</button>
        <div className="loginfooter">
          This website is not affiliated with Discord
        </div>
      </div>
    </div>
  );
};

export default Login;
