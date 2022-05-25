import React from "react";
import "./projects.css";
import cry from "../kuromicry.png";

export default function Projects() {
  return (
    <>
      <div className="ProjectsPage">
        <p className="pagetext">
          In Progress . . .&nbsp;
          <img className="Kuro" src={cry} alt="cry"></img>
        </p>
      </div>
      ;
    </>
  );
}
