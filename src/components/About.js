import React from "react";
import "./about.css";
import { Carousel, Row } from "react-bootstrap";
import pic1 from "../gallery1.jpeg";
import pic2 from "../gallery2.jpeg";
import pic3 from "../gallery3.jpeg";
import pic4 from "../gallery4.jpeg";
import pic5 from "../gallery5.jpeg";

export default function About() {
  return (
    <>
      <div className="AboutPage">
        <Row className="aboutIntro">
          <p className="aboutText"> About Me!</p>
        </Row>
        <div id="myCarousel" class="carouselslide">
          <Row className="carousel">
            <div class="carousel-inner">
              <Carousel variant="dark">
                <Carousel.Item>
                  <img className="d-block w-100" src={pic5} alt="First slide" />
                </Carousel.Item>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src={pic4}
                    alt="Second slide"
                  />
                </Carousel.Item>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    vsrc={pic3}
                    alt="Third slide"
                  />
                </Carousel.Item>
                <Carousel.Item>
                  <img className="d-block w-100" src={pic2} alt="Third slide" />
                </Carousel.Item>
                <Carousel.Item>
                  <img className="d-block w-100" src={pic1} alt="Third slide" />
                </Carousel.Item>
              </Carousel>
            </div>
          </Row>
        </div>
      </div>
      ;
    </>
  );
}
