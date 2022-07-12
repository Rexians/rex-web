import { useNavigate } from "react-router-dom";
import { logout } from "../api/Auth";

export default function useLogOut() {
  // Lougout user and go to /auth
  let navigate = useNavigate();
  const logoutUser = async function () {
    await logout();
    navigate("/auth");
  };
  return { logoutUser };
}
