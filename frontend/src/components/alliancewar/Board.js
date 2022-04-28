import { useState, useRef, useEffect } from "react";
import { warNodes } from "../../api/WarNodes";
import Tiles from "./Tiles";
import NodeSidebar from "./NodeSidebar";
import TierForm from "./TierForm";
import { drawBorders } from "../../helpers/drawBorders";
import "../../styles/alliancewar/Board.css";

const Board = ({ tier }) => {
  // States for board
  const [nodeInfoState, setNodeInfo] = useState({
    show: false,
    expanded: false,
  });
  const [tileNumber, setTileNumber] = useState(0);
  const [warInfo, setWarInfo] = useState({});
  const [nodes, setNodes] = useState({});

  // Get war info when page loads and set state
  const getWarInfo = async function () {
    var response = await warNodes(tier);
    var warInfo = {
      difficulty: response["difficulty"],
      tier: response["tier"],
      tier_multiplier: response["tier_multiplier"],
      tier_rank: response["tier_rank"],
    };
    var allNodes = new Map(Object.entries(response["nodes"]));
    setNodes(allNodes);
    setWarInfo(warInfo);
  };

  useEffect(() => {
    getWarInfo();
  }, []);

  // Draw the board
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#1a1a1a";
      ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
      drawBorders(ctx);
    }
  }, []);

  return (
    <div className="warboard">
      <div className="canvasHolder">
        <TierForm warInfo={warInfo} />
        <canvas ref={canvasRef} id="canvas" width="1263.9" height="2000" />
      </div>
      <Tiles
        nodeInfoState={nodeInfoState}
        setNodeInfo={setNodeInfo}
        tileNumber={tileNumber}
        setTileNumber={setTileNumber}
      />
      {nodeInfoState["show"] && (
        <NodeSidebar
          nodeInfoState={nodeInfoState}
          setNodeInfo={setNodeInfo}
          tileNumber={tileNumber}
          nodes={nodes}
        />
      )}
    </div>
  );
};

export default Board;
