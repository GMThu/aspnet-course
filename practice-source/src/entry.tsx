import React from "react";
import {createRoot} from "react-dom/client";
import Week05 from "./page";
import Week06 from "./week06/page";
const Page=location.pathname.includes("/week06")?Week06:Week05;
createRoot(document.getElementById("root")!).render(<Page/>);
