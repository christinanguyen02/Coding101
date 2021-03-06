import React from "react";
import "./projects.css";
import cube from "../kurocube.png";
import { Row, Col, Card, Container, Button } from "react-bootstrap";
import background from "../blackbackground.jpeg";
import GenZ from "../GenZ.png";

export default function Projects() {
  return (
    <>
      <div className="ProjectsPage">
        <Container fluid>
          <Row>
            <p className="pagetext">
              Projects
              <img className="Kuro" src={cube} alt="cry"></img>
            </p>
            <p></p>
          </Row>
          <Row className="projectcards">
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={GenZ} />
                <Card.Body>
                  <Card.Title>GenZ Trading</Card.Title>
                  <Card.Text>
                    TradeZ is a multi-functional platform for cryptocurrency
                    trading for generation Z.
                  </Card.Text>
                  <Button
                    variant="secondary"
                    href="https://devpost.com/software/tradez-a-genz-crypto-trading-platform"
                    target="_blank"
                  >
                    See More
                  </Button>
                </Card.Body>
              </Card>
            </Col>
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={background} />
                <Card.Body>
                  <Card.Title>In Progress</Card.Title>
                  <Card.Text>...</Card.Text>
                  {/* <Button variant="primary">Go somewhere</Button> */}
                </Card.Body>
              </Card>
            </Col>
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={background} />
                <Card.Body>
                  <Card.Title>In Progress</Card.Title>
                  <Card.Text>...</Card.Text>
                  {/* <Button variant="primary">Go somewhere</Button> */}
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}
