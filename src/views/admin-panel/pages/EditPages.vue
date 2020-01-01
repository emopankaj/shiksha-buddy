<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Add / Edit Pages</strong>
            </b-card-header>
            <b-card-body>
                <b-row class="align-items-center">
                    <b-col cols="6" sm="4" md="2" xl class="mb-3 mb-xl-0">
                        <b-row>
                            <b-button block variant="outline-primary" @click="getAllPages">Primary</b-button>
                        </b-row>
                        <b-row class="mt-3">
                            <b-button block variant="outline-primary">Add New Page</b-button>
                        </b-row>
                    </b-col>
                    <b-col md="6">
                        <b-card>
                            <div slot="header">
                                <strong>Add New Page</strong>
                            </div>
                            <b-form @submit.prevent="addEditPage">
                                <b-form-group
                                        label="Select Page Type"
                                        label-for="pageTypeSelect"
                                        :label-cols="3"
                                >
                                    <b-form-select id="pageTypeSelect" v-model="page.pageType"
                                                   :plain="true"
                                                   :options="[{text: 'Text and Image Page',value: 'textImagePage'},
                                                   {text: 'Contact Page',value: 'contactPage'}]">
                                    </b-form-select>
                                </b-form-group>
                                <b-form-group
                                        description="Enter Name of the Page"
                                        label="Page Name"
                                        label-for="pageName"
                                        :label-cols="3"
                                >
                                    <b-form-input id="pageName" type="text" placeholder="Page Name"
                                                  v-model="page.page_name"></b-form-input>
                                </b-form-group>
                                <b-form-group
                                        description="Enter Page Title"
                                        label="Page Title"
                                        label-for="pageTitle"
                                        :label-cols="3"
                                >
                                    <b-form-input id="pageTitle" type="text" placeholder="Page Title"
                                                  v-model="page.title"></b-form-input>
                                </b-form-group>
                                <b-form-group
                                        description="Enter Page Heading"
                                        label="Page Heading"
                                        label-for="pageHeading"
                                        :label-cols="3"
                                >
                                    <b-form-input id="pageHeading" type="text"
                                                  placeholder="Page Heading" v-model="page.heading"></b-form-input>
                                </b-form-group>
                                <template v-if="false">
                                    <b-form-group
                                            description="Select Image to be shown on the page"
                                            label="Image"
                                            label-for="pageImage"
                                            :label-cols="3"
                                    >
                                        <b-form-file id="pageImage" :plain="true"
                                                     v-model="page.pageImage"></b-form-file>
                                    </b-form-group>
                                    <b-form-group
                                            label="Page Content"
                                            label-for="pageContent"
                                            :label-cols="3"
                                    >
                                        <b-form-textarea id="pageContent" :rows="9"
                                                         placeholder="Content to be shown on the Page"
                                                         v-model="page.content"></b-form-textarea>
                                    </b-form-group>
                                </template>
                                <template v-else>
                                    <b-form-group
                                            description="Enter Latitude for the location"
                                            label="Location Latitude"
                                            label-for="latitude"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="latitude" type="text"
                                                      placeholder="Latitude" v-model="page.latitude"></b-form-input>
                                    </b-form-group>
                                    <b-form-group
                                            description="Enter Longitude for the location"
                                            label="Location Longitude"
                                            label-for="longitude"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="longitude" type="text"
                                                      placeholder="Longitude" v-model="page.longitude"></b-form-input>
                                    </b-form-group>
                                    <b-form-group
                                            description="Enter Phone Number"
                                            label="Phone Number"
                                            label-for="phoneNumber"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="phoneNumber" type="text"
                                                      placeholder="Phone Number"
                                                      v-model="page.phone"></b-form-input>
                                    </b-form-group>
                                    <b-form-group
                                            description="Please enter your email"
                                            label="Email"
                                            label-for="emailAddress"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="emailAddress" type="email" placeholder="Enter your email"
                                                      autocomplete="email" v-model="page.email"/>
                                    </b-form-group>
                                    <b-form-group
                                            description="Enter Facebook Page link"
                                            label="Facebook Page Link"
                                            label-for="facebookPageLink"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="facebookPageLink" type="text"
                                                      placeholder="Facebook Page Link" v-model="page.facebook_link"/>
                                    </b-form-group>
                                    <b-form-group
                                            description="Enter Twitter Link"
                                            label="Twitter Link"
                                            label-for="twitterLink"
                                            :label-cols="3"
                                    >
                                        <b-form-input id="twitterLink" type="text"
                                                      placeholder="Twitter Link" v-model="page.twitter_link"/>
                                    </b-form-group>
                                    <b-form-group
                                            label="Address"
                                            label-for="postalAddress"
                                            :label-cols="3"
                                    >
                                        <b-form-textarea id="postalAddress" :rows="9"
                                                         placeholder="Address to be shown on Contact page"
                                                         v-model="page.address"/>
                                    </b-form-group>
                                </template>

                                <div slot="footer">
                                    <b-button type="submit" size="sm" variant="primary"><i
                                            class="fa fa-dot-circle-o"></i> Submit
                                    </b-button>
                                    <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i> Reset
                                    </b-button>
                                </div>
                            </b-form>
                        </b-card>
                    </b-col>
                </b-row>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'edit-pages',
        data() {
            return {
                page:
                    {
                        id: '',
                        // FIXME: remove this
                        'site_id': 'dummy',
                        pageType: 'textImagePage',
                        page_name: '',
                        title: '',
                        heading: '',
                        content: '',
                        latitude: '',
                        longitude: '',
                        phone: '',
                        email: '',
                        facebook_link: '',
                        twitter_link: '',
                        address: ''
                    }
            }
        },
        methods: {
            addEditPage: function () {
                axios.post('/api/page/', this.page)
                    .then(response => console.log(response))
                    .catch(error => console.log(error))
            },
            getAllPages: function () {
                axios.get('/api/page/')
                    .then(response => console.log(response))
                    .catch(error => console.log(error))
            }
        }
    }
</script>
