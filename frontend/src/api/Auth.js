const auth = async function () {
  const response = await fetch("http://localhost:5000/authenticated", {
    credentials: "include",
  });
  const responseData = await response.json();
  return responseData;
};

const logout = async function () {
  await fetch("http://localhost:5000/logout", {
    method: "POST",
    credentials: "include",
  });
};

export { auth, logout };
