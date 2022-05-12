const auth = async function () {
  const response = await fetch("http://127.0.0.1:5000/authenticated");
  const responseData = await response.json();
  return responseData;
};

export { auth };
