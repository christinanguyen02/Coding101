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
                <p className="Body">
                  Hi! :) <br></br>Welcome to my website! <br></br>I'm Christina
                  Nguyen! :)
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
