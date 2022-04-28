const warNodes = async function (tier) {
  // Get war info
  const response = await fetch(`http://127.0.0.1:5000/war/${tier}`);
  const responseData = await response.json();
  return responseData;
};

export { warNodes };
