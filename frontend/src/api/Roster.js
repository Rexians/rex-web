const addChamp = async function (champ, tier, rank) {
  await fetch(
    `http://localhost:5000/roster/add?champ=${champ}&tier=${tier}&rank=${rank}`,
    { method: "POST", mode: "no-cors", credentials: "include" }
  );
};

const getChamp = async function (champId, tier) {
  const response = await fetch(
    `http://localhost:5000/roster/champ?champ-id=${champId}&tier=${tier}`,
    {
      credentials: "include",
    }
  );
  const responseData = await response.json();
  return responseData;
};

const getChampsDisplay = async function () {
  const response = await fetch("http://localhost:5000/roster/champs/imgs", {
    credentials: "include",
  });
  const responseData = await response.json();
  return responseData;
};

const getLatestChampDisplay = async function () {
  const response = await fetch(
    "http://localhost:5000/roster/champs/imgs/latest",
    {
      credentials: "include",
    }
  );
  const responseData = await response.json();
  return responseData;
};

export { addChamp, getChamp, getChampsDisplay, getLatestChampDisplay };
