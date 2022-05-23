import { Container, Row, Col } from "react-bootstrap";
import Christina from "./christina.jpeg";
import "./App.css";

function App() {
  return (
    <>
      <div className="App">
        <header className="App-header">
          <Container fluid>
            <Row>
              <Col>
                {" "}
                <img src={Christina} className="Main-photo" alt="" />
                <p>Picture taken at Japanese Tea Garden.</p>{" "}
              </Col>
              <Col className="Intro">
                <h1>Hi! I'm Christina Nguyen</h1>
                <p className="Body">
                  welcome to my website :) it is a work in progress
                  <p>don't judge, i'm a newbie coder</p>
                </p>
              </Col>
            </Row>
          </Container>
        </header>
      </div>
    </>
  );
}

export default App;
