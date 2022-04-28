import "../../styles/alliancewar/Tiles.css";

const Tiles = ({ nodeInfoState, setNodeInfo, tileNumber, setTileNumber }) => {
  const show = function (e) {
    var clickedTileNumber = parseInt(e.currentTarget.innerHTML);
    var top = window.pageYOffset || document.documentElement.scrollTop;
    var expand = false;

    // First check if scrolled, auto expand sidebar when tile is clicked
    // Initial click, set sidebar to true. If clicked node is same as current sidebar node, remove sidebar.
    // If clicked tile is different, show new nod sidebar
    if (top > 4) {
      expand = true;
    } else {
      expand = false;
    }
    if (tileNumber === 0) {
      setNodeInfo({ show: true, expanded: expand });
    } else if (clickedTileNumber === tileNumber) {
      setNodeInfo({ show: !nodeInfoState["show"], expanded: expand });
    } else {
      setNodeInfo({ show: true, expanded: expand });
    }
    setTileNumber(clickedTileNumber);
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
