<template>
    <b-card v-if="visible">
        <div slot="header">
            <strong>Edit Page</strong>
        </div>
        <b-row>
            <b-col>
                <b-form @submit.prevent="addEditPage">
                    <b-form-group
                            label="Select Page Type"
                            label-for="pageTypeSelect"
                            :label-cols="3"
                    >
                        <b-form-select id="pageTypeSelect" v-model="currentPage.pageType"
                                       :plain="true"
                                       :options="[{text: 'Text and Image Page',value: 'TextImagePage'},
                                                   {text: 'Contact Page',value: 'ContactPage'}]">
                        </b-form-select>
                    </b-form-group>
                    <b-form-group
                            description="Enter Name of the Page"
                            label="Page Name"
                            label-for="pageName"
                            :label-cols="3"
                    >
                        <b-form-input id="pageName" type="text" placeholder="Page Name"
                                      v-model="currentPage.page_name"></b-form-input>
                    </b-form-group>
                    <b-form-group
                            description="Enter Page Title"
                            label="Page Title"
                            label-for="pageTitle"
                            :label-cols="3"
                    >
                        <b-form-input id="pageTitle" type="text" placeholder="Page Title"
                                      v-model="currentPage.title"></b-form-input>
                    </b-form-group>
                    <b-form-group
                            description="Enter Page Heading"
                            label="Page Heading"
                            label-for="pageHeading"
                            :label-cols="3"
                    >
                        <b-form-input id="pageHeading" type="text"
                                      placeholder="Page Heading"
                                      v-model="currentPage.heading"></b-form-input>
                    </b-form-group>
                    <template v-if="currentPage.pageType==='TextImagePage'">
                        <b-form-group
                                description="Select Image to be shown on the page"
                                label="Image"
                                label-for="pageImage"
                                :label-cols="3"
                        >
                            <b-form-file id="pageImage" :plain="true"
                                         v-model="currentPage.pageImage"></b-form-file>
                        </b-form-group>
                        <b-form-group
                                label="Page Content"
                                label-for="pageContent"
                                :label-cols="3"
                        >
                            <b-form-textarea id="pageContent" :rows="9"
                                             placeholder="Content to be shown on the Page"
                                             v-model="currentPage.text"></b-form-textarea>
                        </b-form-group>
                    </template>
                    <template v-else>
                        <b-form-group
                                description="Enter -1 if you don't want latitude"
                                label="Location Latitude"
                                label-for="latitude"
                                :label-cols="3"
                        >
                            <b-form-input id="latitude" type="text"
                                          placeholder="Latitude"
                                          v-model="currentPage.latitude"></b-form-input>
                        </b-form-group>
                        <b-form-group
                                description="Enter -1 if you don't want longitude"
                                label="Location Longitude"
                                label-for="longitude"
                                :label-cols="3"
                        >
                            <b-form-input id="longitude" type="text"
                                          placeholder="Longitude"
                                          v-model="currentPage.longitude"></b-form-input>
                        </b-form-group>
                        <b-form-group
                                description="Enter Phone Number"
                                label="Phone Number"
                                label-for="phoneNumber"
                                :label-cols="3"
                        >
                            <b-form-input id="phoneNumber" type="text"
                                          placeholder="Phone Number"
                                          v-model="currentPage.phone"></b-form-input>
                        </b-form-group>
                        <b-form-group
                                description="Please enter your email"
                                label="Email"
                                label-for="emailAddress"
                                :label-cols="3"
                        >
                            <b-form-input id="emailAddress" type="email" placeholder="Enter your email"
                                          autocomplete="email" v-model="currentPage.email"/>
                        </b-form-group>
                        <b-form-group
                                description="Enter Facebook Page link"
                                label="Facebook Page Link"
                                label-for="facebookPageLink"
                                :label-cols="3"
                        >
                            <b-form-input id="facebookPageLink" type="text"
                                          placeholder="Facebook Page Link"
                                          v-model="currentPage.facebook_link"/>
                        </b-form-group>
                        <b-form-group
                                description="Enter Twitter Link"
                                label="Twitter Link"
                                label-for="twitterLink"
                                :label-cols="3"
                        >
                            <b-form-input id="twitterLink" type="text"
                                          placeholder="Twitter Link"
                                          v-model="currentPage.twitter_link"/>
                        </b-form-group>
                        <b-form-group
                                label="Address"
                                label-for="postalAddress"
                                :label-cols="3"
                        >
                            <b-form-textarea id="postalAddress" :rows="9"
                                             placeholder="Address to be shown on Contact page"
                                             v-model="currentPage.address"/>
                        </b-form-group>
                    </template>

                    <div slot="footer">
                        <b-button type="submit" size="sm" variant="primary"><i
                                class="fa fa-dot-circle-o"></i> Submit
                        </b-button>
                        <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i>
                            Reset
                        </b-button>
                    </div>
                </b-form>
            </b-col>
        </b-row>
    </b-card>
</template>

<script>
    import axios from 'axios';
    import {EventBus} from '@/main';

    export default {
        name: 'edit-page-form',
        props: {
            visible: Boolean,
            page: Object
        },
        data() {
            return {currentPage: {...this.page}}
        },
        methods: {
            addEditPage: function () {
                // if id is present, it should be a page update otherwise page create

                if (this.currentPage.id) {
                    axios.put('/api/page/', this.currentPage)
                        .then(response => console.log(response))
                        .catch(error => console.log(error))
                } else {
                    axios.post('/api/page/', this.currentPage)
                        .then(response => console.log(response))
                        .catch(error => console.log(error))
                }
                EventBus.$emit('refresh-pages');
            }
        }
    }
</script>