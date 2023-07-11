import React from "react";
import "./resume.css";
import resumePic from "../ResumeUT.png";
import { Container, Row } from "react-bootstrap";
import pdf from "../ResumeUT.pdf";
import cube from "../kurocube.png";

export default function Resume() {
  return (
    <>
      <div className="ResumePage">
        <Container fluid>
          <Row className="intro">
            <p className="Text">
              {" "}
              Resume&nbsp;
              <img src={cube} className="cuberomi" alt="" />
            </p>
          </Row>
          <div className="picture">
            <a href={pdf} target="_blank" rel="noreferrer">
              <Row>
                <img src={resumePic} className="pic" alt="" />
              </Row>
            </a>
            <p>last updated July 2023</p>
          </div>
          <Row className="footer">
            <p></p>
          </Row>
        </Container>
      </div>
      ;
    </>
  );
}
