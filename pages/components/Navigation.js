import React from "react"
import { Nav, Navbar, Container } from "react-bootstrap"
import styles from '../../styles/Navigation.module.css'


export default function Navigation(){
    return(

        <Navbar variant="light" className={styles.navbarMain}>
            <Container>
                <Navbar.Brand href="#home" className={styles.navbarBrand}>Navbar</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="#home">Home</Nav.Link>
                    <Nav.Link href="#features">Features</Nav.Link>
                    <Nav.Link href="#pricing">Pricing</Nav.Link>
                </Nav>
            </Container>
      </Navbar>

    )
}

