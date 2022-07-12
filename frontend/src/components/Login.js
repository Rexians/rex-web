import Navigation from "./Navigation";
import "../styles/Login.css";

const Login = () => {
  return (
    <div>
      <Navigation />
      <div className="login-form">
        <div className="login-header"></div>
        <a
          href="https://discord.com/api/oauth2/authorize?client_id=940833443074441256&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth%2Fcallback&response_type=code&scope=identify"
          className="login-button"
        >
          Login through Discord
        </a>
        <div className="login-footer">
          This website is not affiliated with Discord
        </div>
      </div>
    </div>
  );
};

export default Login;
