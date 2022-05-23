import React from "react";
import "./header.css";
import { Container, Navbar, Nav, NavLink } from "react-bootstrap";
export default function Header() {
  return (
    <div>
      <Navbar className="MainNav">
        <Container className="container">
          <Navbar.Brand className="Name" href="/">
            Christina Nguyen
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Nav className="NavLinks">
            <NavLink href="/about">About</NavLink>
            <NavLink href="/resume">Resume</NavLink>
            <NavLink href="/projects">Projects</NavLink>
          </Nav>
        </Container>
      </Navbar>
    </div>
  );
}
