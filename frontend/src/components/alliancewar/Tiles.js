import "../../styles/alliancewar/Tiles.css";

const Tiles = ({ nodeInfoState, showNodeInfo, nodeNumber, setNodeNumber }) => {

  // Show node sidebar when tile is clicked
  const show = function (e) {
    var tileNumber = parseInt(e.currentTarget.innerHTML);
    // Initial click, set sidebar to true. If clicked node is same as current sidebar node, remove sidebar.
    // If clicked tile is different, show new nod sidebar
    if (nodeNumber === 0) {
      showNodeInfo(true);
    } else if (tileNumber === nodeNumber) {
      showNodeInfo(!nodeInfoState);
    } else {
      showNodeInfo(true);
    }
    setNodeNumber(tileNumber);
  };

  // Create the buttons
  const addButtons = function () {
    const buttons = [];
    for (var tile = 1; tile < 56; tile++) {
      buttons.push(
        <button key={tile} className="tile" id={`tile${tile}`} onClick={show}>
          {tile}
        </button>
      );
    }
    return buttons;
  };

  return <>{addButtons()}</>;
};

export default Tiles;
