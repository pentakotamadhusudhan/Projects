const mongoose = require('mongoose');
const express = require('express');
const swaggerJsDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
const { json } = require('body-parser')
const app = express()
const checkAuth = require('./jwt_token')
const url = "mongodb://localhost:27017/CrudDB"
mongoose.connect(url, {useNewUrlParser:true})
const con = mongoose.connection


con.on('open', (datab) => {
    console.log('connection.....')
    
    const swaggerOptions = {
        swaggerDefinition: {
            openapi: '3.0.0',
            info: {
                title: 'Student API',
                version: '1.0.0',
                description: "Student API information",
                servers: [{url:'http://localhost:3000'}],
                
            },
            components: {
                securitySchemes: {
                  bearerAuth: {
                    type: 'http',
                    scheme: 'bearer',
                    bearerFormat: 'JWT',
                  }
                }
              },
              security: [{
                bearerAuth: []
              }]
        },
        apis: ["database.js"]
    }

    const swaggerDocs = swaggerJsDoc(swaggerOptions)
    app.use('/api-doc', swaggerUi.serve, swaggerUi.setup(swaggerDocs))

    /**
     * @swagger
     * /user:
     *    get:
     *      description: Use to request all customers
     *      summary: Get the users
     *      tags: [User]
     *      responses:
     *          '200':
     *              description: A successful response
     *              content:
     *                  application/json:
     *                      
     *                          
     * /user/{id}:
     *    get:
     *      summary: Get the user data by id
     *      description: Get the user data by id
     *      tags: [User]
     *      parameters:
     *        - in: path
     *          name: id
     *          required: true
     *          schema:
     *              type: integer
     *      responses:
     *          '200':
     *              description: successfull
     * /api/token:
     *    post:
     *      summary: Token generation
     *      tags: [api]
     *      produces:
     *          - application/json
     *      consumes:
     *          - application/json
     *      responses:
     *            '200':
     *              description: Successfull
     * /userpost:
     *    post:
     *      summary: Create a new user
     *      tags: [User]
     *      produces:
     *          - application/json
     *      consumes:
     *          - application/json
     *      parameters:
     *          - in: body
     *            name: body
     *            required: true
     *            schema:
     *              type: object
     *              properties:
     *                  id:
     *                      type: number
     *                  Firstname:
     *                      type: string
     *                  Lastname:
     *                      type: string
     *                  Email:
     *                      type: string
     *                  Username:
     *                      type: string
     *                  Password:
     *                      type: string
     *                  MobileNumber:
     *                      type: string
     *                  DeviceToken:
     *                      type: string
     *      responses:
     *          200:
     *              description: successful
     * /userupdate/{id}:
     *    put:
     *        summary: Create a new user
     *        tags: [User]
     *        produces:
     *            - application/json
     *        consumes:
     *            - application/json
     *        parameters:
     *            - name: id
     *              description: Using id to update
     *              in: path
     *              type: interger
     *              required: true
     *            - name: reqBody
     *              description: Request body
     *              in: body
     *              schema:
     *                 type: object
     *                 properties:
     *                    Firstname:
     *                        type: string
     *                    Lastname:
     *                        type: string
     *                    Email:
     *                        type: string
     *                    Username:
     *                        type: string
     *                    Password:
     *                        type: string
     *                    MobileNumber:
     *                        type: string
     *                    DeviceToken:
     *                        type: string
     *        responses:
     *            200:
     *                description: Successful
     *        
     *        
     *
     */

    app.use(express.json())
    const userdata = require('./user')
    app.use('/user',userdata)
    const Userpost = require('./userPost')
    app.use('/userpost',Userpost)
    const update = require('./UserUpdate')
    app.use('/userupdate',update)
    const userdataget = require('./userbyid')
    app.use('/user',userdataget)
    const token = require('./login')
    app.use('/api', token)
    
})
app.listen(3000, () => console.log('listening......'));
