describe("Test Login", () => {
    beforeEach(() => {
        cy.visit('http://localhost:8000/login')
    })

    it("Test Login", () => {
        cy.get("#id_username").type("test_user").should("have.value", "test_user")
        cy.get("#id_password").type("Pass1234!").should('have.value', "Pass1234!")
        cy.get('input[type="submit"]').click()
    })

})