describe("Test Register", () => {
    beforeEach(() => {
        cy.visit('http://127.0.0.1:8000/signup/')
    })

    it("Test Login", () => {
        cy.get("#id_username").type("test_user1").should("have.value", "test_user1")
        cy.get("#id_password1").type("Pass1234!").should('have.value', "Pass1234!")
        cy.get("#id_password2").type("Pass1234!").should('have.value', "Pass1234!")
        cy.get('button[type="submit"]').click()
    })

})