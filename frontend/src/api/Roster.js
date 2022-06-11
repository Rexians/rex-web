const addChamp = async function (champ, tier, rank) {
  await fetch(
    `http://localhost:5000/roster/add?champ=${champ}&tier=${tier}&rank=${rank}`,
    { method: "POST", mode: "no-cors", credentials: "include" }
  );
};

const getChamps = async function () {
  const response = await fetch("http://localhost:5000/roster/champs/imgs", {
    credentials: "include",
  });
  const responseData = await response.json();
  return responseData;
};

export { addChamp, getChamps };
