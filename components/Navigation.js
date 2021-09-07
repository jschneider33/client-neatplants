import React from "react"
import Link from "next/link"
import { Nav, Navbar, Container } from "react-bootstrap"
import styles from '../styles/Navigation.module.sass'

export default function Navigation(){
    return(
        <Navbar aria-label="primary" className={styles.main}>
            <Container className={styles.navCont}>
                <Navbar.Brand href="/" className={styles.brand}>Neat <br/>Houseplants</Navbar.Brand>
                <Nav className={`me-auto ${styles.navItems}`}>
                    <Link href="/">
                        <a className={styles.navLink}>Home</a>
                    </Link>
                    <Link href="/shop">
                        <a className={styles.navLink}>Shop</a>
                    </Link>
                </Nav>
            </Container>
      </Navbar>
    )
}

