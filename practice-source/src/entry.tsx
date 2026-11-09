import React from "react";
import {createRoot} from "react-dom/client";
import Week05 from "./page";
import Week06 from "./week06/page";
import SimpleWeek06 from "./week06/simple";
const Page=location.pathname.includes("/week06/simple")?SimpleWeek06:location.pathname.includes("/week06")?Week06:Week05;
createRoot(document.getElementById("root")!).render(<Page/>);
