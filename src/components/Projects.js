import React from "react";
import "./projects.css";
import cube from "../kurocube.png";
import { Row, Col, Card, Container, Button } from "react-bootstrap";
import background from "../blackbackground.jpeg";
import GenZ from "../GenZ.png";
import Animation from "../Animation.png";
import Pong from "../PongGame.png";

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
                <Card.Img variant="top" src={Animation} />
                <Card.Body>
                  <Card.Title>Graphic Animation</Card.Title>
                  <Card.Text>
                    Graphic Animation created using javascript and processing
                    for a class assignment.
                  </Card.Text>
                  {
                    <Button
                      variant="secondary"
                      href="https://github.com/Abdon02/cs324eCAS/tree/main/group_3_assignment4"
                      target="_blank"
                    >
                      See More
                    </Button>
                  }
                </Card.Body>
              </Card>
            </Col>
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={Pong} />
                <Card.Body>
                  <Card.Title>Pong Game</Card.Title>
                  <Card.Text>
                    Pong is a simulation of table tennis game created using
                    javascript and processing for a class project.
                  </Card.Text>
                  {
                    <Button
                      variant="secondary"
                      href="https://drive.google.com/file/d/1eOe_mn0ogun7xgGD17XEJwJRwchVuEGZ/view?usp=share_link"
                      target="_blank"
                    >
                      See More
                    </Button>
                  }
                </Card.Body>
              </Card>
            </Col>
          </Row>
          <Row>
            <p></p>
          </Row>
          {/* second row of projects */}
          <Row className="projectcards">
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={background} />
                <Card.Body>
                  <Card.Title>In Progress</Card.Title>
                  <Card.Text>...</Card.Text>
                  {/* <Button
                    variant="secondary"
                    href=""
                    target="_blank"
                  >
                    See More
                  </Button>   */}
                </Card.Body>
              </Card>
            </Col>
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={background} />
                <Card.Body>
                  <Card.Title>In Progress</Card.Title>
                  <Card.Text>...</Card.Text>
                  {/* <Button
                    variant="secondary"
                    href=""
                    target="_blank"
                  >
                    See More
                  </Button>   */}
                </Card.Body>
              </Card>
            </Col>
            <Col className="single" align="center">
              <Card style={{ width: "25rem" }}>
                <Card.Img variant="top" src={background} />
                <Card.Body>
                  <Card.Title>In Progress</Card.Title>
                  <Card.Text>...</Card.Text>
                  {/* <Button
                    variant="secondary"
                    href=""
                    target="_blank"
                  >
                    See More
                  </Button>   */}
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}
