<template>
    <b-card>
        <div slot="header">
            <strong>Edit Menu Item</strong>
        </div>
        <b-row>
            <b-col>
                <b-form @submit.prevent="submitForm">
                    <b-form-group
                            description="Enter text to be shown on the current item"
                            label="Menu Item Text"
                            label-for="menuItemText"
                            :label-cols="3"
                    >
                        <b-form-input id="menuItemText" type="text" placeholder="Menu Item Text"
                                      v-model="currentMenuItem.label"></b-form-input>
                    </b-form-group>
                    <b-form-group
                            label="Linked Page"
                            label-for="basicRadiosCustom"
                            :label-cols="3"
                    >
                        <b-form-radio-group
                                id="basicRadiosCustom"
                                value="1"
                                stacked>
                            <div class="custom-control custom-radio" v-for="page in availablePages"
                                 :key="page.pageType + page.id">
                                <input type="radio" :id="'pageRadio'+page.pageType + page.id"
                                       class="custom-control-input" name="menuItemPage"
                                       :value="page" v-model="currentMenuItem.linked_page">
                                <label class="custom-control-label"
                                       :for="'pageRadio'+ page.pageType + page.id">{{page.page_name}}</label>
                            </div>
                        </b-form-radio-group>
                    </b-form-group>
                    <div slot="footer">
                        <b-button type="submit" size="sm" variant="primary"><i
                                class="fa fa-dot-circle-o"></i> Save
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
    import {EventBus} from '@/main';
    import PageMixin from "../mixins/PageMixin";

    export default {
        name: 'menu-edit-form',
        mixins: [PageMixin],
        props: {
            menuItem: Object
        },
        data() {
            return {
                availablePages: []
            };
        },
        computed: {
            currentMenuItem() {
                return this.menuItem;
            }
        },
        methods: {
            submitForm() {
                EventBus.$emit('update-menu-item', this.data.currentMenuItem);
            }
        },
        mounted() {
            this.getAllPages((pages) => this.availablePages = pages);
        }
    }
</script>
