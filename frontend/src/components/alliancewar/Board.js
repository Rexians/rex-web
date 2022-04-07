import { useState, useRef, useEffect } from "react";
import Tiles from "./Tiles";
import NodeSidebar from "./NodeSidebar";
import "../../styles/alliancewar/Board.css";

const Board = () => {

  // States for nodes
  const [nodeInfoState, showNodeInfo] = useState(false);
  const [nodeNumber, setNodeNumber] = useState(0);


  // The war board with all the tiles and canvas
  const canvasRef = useRef(null);

  const drawLines = function (ctx, canvas) {
    const width = canvas.width;
    const height = canvas.height;

    // ctx.strokeStyle = "#2596be";
    // ctx.beginPath();
    // ctx.lineWidth = 3;
    // ctx.setLineDash([2, 5]);
    // ctx.moveTo(348, 200);
    // ctx.lineTo(450, 50);
    // ctx.stroke();
  };

  const drawBorders = function (ctx, canvas) {
    const img = new Image();
    img.onload = function () {
      ctx.drawImage(img, 767, 34); //55
      ctx.drawImage(img, 434, 34); //54
      ctx.drawImage(img, 893, 174); //53
      ctx.drawImage(img, 601, 150); //52
      ctx.drawImage(img, 308, 174); //51
      ctx.drawImage(img, 793, 314); //50
      ctx.drawImage(img, 601, 314); //49
      ctx.drawImage(img, 409, 314); //48
      ctx.drawImage(img, 1020, 455); //47
      ctx.drawImage(img, 181, 455); //46
      ctx.drawImage(img, 1146, 546); //45
      ctx.drawImage(img, 1020, 601); //44
      ctx.drawImage(img, 893, 546); //43
      ctx.drawImage(img, 308, 546); //42
      ctx.drawImage(img, 181, 601); //41
      ctx.drawImage(img, 55, 546); //40
      ctx.drawImage(img, 601, 576); //39
      ctx.drawImage(img, 717, 674); //38
      ctx.drawImage(img, 601, 729); //37
      ctx.drawImage(img, 485, 674); //36
      ctx.drawImage(img, 1146, 802); //35
      ctx.drawImage(img, 1020, 747); //34
      ctx.drawImage(img, 893, 802); //33
      ctx.drawImage(img, 308, 802); //32
      ctx.drawImage(img, 181, 747); //31
      ctx.drawImage(img, 55, 802); //30
      ctx.drawImage(img, 601, 875); //29
      ctx.drawImage(img, 717, 930); //28
      ctx.drawImage(img, 485, 930); //27
      ctx.drawImage(img, 893, 1021); //26
      ctx.drawImage(img, 601, 1021); //25
      ctx.drawImage(img, 308, 1021); //24
      ctx.drawImage(img, 601, 1131); //23
      ctx.drawImage(img, 601, 1241); //22
      ctx.drawImage(img, 1020, 1332); //21
      ctx.drawImage(img, 181, 1332); //20
      ctx.drawImage(img, 601, 1369); //19
      ctx.drawImage(img, 1146, 1423); //18
      ctx.drawImage(img, 1020, 1478); //17
      ctx.drawImage(img, 893, 1423); //16
      ctx.drawImage(img, 308, 1423); //15
      ctx.drawImage(img, 181, 1478); //14
      ctx.drawImage(img, 55, 1423); //13
      ctx.drawImage(img, 717, 1466); //12
      ctx.drawImage(img, 601, 1521); //11
      ctx.drawImage(img, 485, 1466); //10
      ctx.drawImage(img, 1146, 1680); //9
      ctx.drawImage(img, 1020, 1625); //8
      ctx.drawImage(img, 893, 1680); //7
      ctx.drawImage(img, 308, 1680); //6
      ctx.drawImage(img, 181, 1625); //5
      ctx.drawImage(img, 55, 1680); //4
      ctx.drawImage(img, 717, 1722); //3
      ctx.drawImage(img, 601, 1667); //2
      ctx.drawImage(img, 485, 1722); //1
    };
    img.src = require("../../assets/Border.png");
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#1a1a1a";
      ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
      drawLines(ctx, canvas);
      drawBorders(ctx, canvas);
    }
  }, []);

  return (
    <div className="warboard">
      <div className="canvasHolder">
        <div className="awtitle">Alliance War</div>
        <canvas ref={canvasRef} id="canvas" width="1263.9" height="2000" />
      </div>
      <Tiles
        nodeInfoState={nodeInfoState}
        showNodeInfo={showNodeInfo}
        nodeNumber={nodeNumber}
        setNodeNumber={setNodeNumber}
      />
      {nodeInfoState && <NodeSidebar nodeNumber={nodeNumber} />}
    </div>
  );
};

export default Board;
