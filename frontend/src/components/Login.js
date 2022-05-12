import Navigation from "./Navigation";
import "../styles/Login.css";

const Login = () => {
  return (
    <div>
      <Navigation />
      <div className="loginform">
        <div className="loginheader"></div>
        <a
          href="https://discord.com/api/oauth2/authorize?client_id=940833443074441256&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth%2Fcallback&response_type=code&scope=identify"
          className="loginbutton"
        >
          Login through Discord
        </a>
        <div className="loginfooter">
          This website is not affiliated with Discord
        </div>
      </div>
    </div>
  );
};

export default Login;
