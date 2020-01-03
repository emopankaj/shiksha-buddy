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
                                      v-model="current_menu_item.menu_label"></b-form-input>
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
                            <div class="custom-control custom-radio" v-for="page in available_pages" :key="page.id">
                                <input type="radio" :id="'pageRadio' + page.id" name="customRadio"
                                       class="custom-control-input"
                                       :value="page.id">
                                <label class="custom-control-label"
                                       :for="'pageRadio' + page.id">{{page.page_name}}</label>
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
            item_id: String
        },
        data() {
            return {
                current_menu_item: {
                    menu_item_id: this.item_id,
                    menu_label: '',
                    linked_page: {}
                },
                available_pages: [{page_id: 1, page_name: 'page 1'}, {page_id: 2, page_name: 'page 2'}]
            };
        },
        methods: {
            submitForm() {
                EventBus.$emit('update-menu-item', this.data.current_menu_item);
            }
        },
        mounted() {
            this.getAllPages((pages) => {
                this.available_pages = Object.keys(pages).reduce(function (r, k) {
                    return r.concat(k, pages[k]);
                }, []);
            });
        }
    }
</script>
