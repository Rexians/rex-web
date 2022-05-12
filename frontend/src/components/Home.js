import Navigation from "./Navigation";
import "../styles/Home.css";

const Home = () => {
  return (
    <div className="homecontainer">
      {window.localStorage.getItem("logged") === "false" ? (
        <Navigation />
      ) : (
        "None"
      )}
    </div>
  );
};

export default Home;
