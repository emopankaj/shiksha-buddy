<template>
    <div class="animated fadeIn">
        <b-card no-body>
            <b-card-header>
                <strong>Edit Menu</strong>
            </b-card-header>
            <b-card-body>
                <nested-draggable :menu="menuStructure" :order="1"/>
            </b-card-body>
        </b-card>
        <menu-edit-form :menuItem="currentMenuItem"/>
    </div>
</template>

<script>
    import MenuEditForm from "./MenuEditForm";
    import {EventBus} from "@/main";
    import NestedDraggable from "@/views/admin-panel/infra/NestedDraggable";

    export default {
        name: 'menu-edit',
        components: {
            NestedDraggable,
            MenuEditForm,
        },
        data() {
            return {
                currentMenuItem: {},
                menuStructure: []
            };
        },
        methods: {
            addMenu() {
                this.menuStructure = [...this.menuStructure,
                    {
                        id: this.menuStructure.length + 1,
                        label: 'Change this Text',
                        type: 'intermediate_menu',
                        menus: [],
                        linked_page: {}
                    }];
            },
            updateMenuItem(menuItem) {
                let updatedMenuItem = menuItem;
                let index = this.menuStructure.findIndex(menu => menu.id === updatedMenuItem.id);

                if (index !== -1) {
                    this.menuStructure.$set(index, updatedMenuItem);
                } else {
                    this.menuStructure.push(updatedMenuItem);
                }
            },
            initMenuStructure() {
                this.menuStructure = [{
                    id: 1,
                    label: 'first order',
                    type: 'intermediate_menu',
                    menus: [
                        {
                            id: 11,
                            label: 'second order',
                            type: 'intermediate_menu',
                            menus: [
                                {
                                    id: 111,
                                    label: 'third order 1',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                },
                                {
                                    id: 112,
                                    label: 'third order 2',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                },
                                {
                                    id: 112,
                                    label: 'third order 3',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                }
                            ]
                        },
                        {
                            id: 12,
                            label: 'second order',
                            type: 'page_menu',
                            linked_page: {
                                id: 2,
                                page_name: '',
                                pageType: ''
                            }
                        },
                        {
                            id: 13,
                            label: 'second order',
                            type: 'page_menu',
                            menus: [{
                                    id: 111,
                                    label: 'third order 1',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                },
                                {
                                    id: 112,
                                    label: 'third order 2',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                },
                                {
                                    id: 112,
                                    label: 'third order 3',
                                    type: 'page_menu',
                                    menus: [],
                                    linked_page: {
                                        id: 2,
                                        page_name: '',
                                        pageType: ''
                                    }
                                }],
                            linked_page: {
                                id: 2,
                                page_name: '',
                                pageType: ''
                            }
                        }
                    ]
                },
                    {
                        id: 2,
                        label: 'first order',
                        type: 'intermediate_menu',
                        menus: [
                            {
                                id: 21,
                                label: 'second order',
                                type: 'intermediate_menu',
                                menus: [
                                    {
                                        id: 211,
                                        label: 'third order',
                                        type: 'page_menu',
                                        menus: [],
                                        linked_page: {
                                            id: 2,
                                            page_name: '',
                                            pageType: ''
                                        }
                                    }
                                ]
                            },
                            {
                                id: 22,
                                label: 'second order',
                                type: 'page_menu',
                                menus: [],
                                linked_page: {
                                    id: 2,
                                    page_name: '',
                                    pageType: ''
                                }
                            }
                        ]
                    },
                    {
                        id: 3,
                        label: 'first order',
                        type: 'intermediate_menu',
                        menus: [
                            {
                                id: 31,
                                label: 'second order',
                                type: 'intermediate_menu',
                                menus: [
                                    {
                                        id: 311,
                                        label: 'third order',
                                        type: 'page_menu',
                                        menus: [],
                                        linked_page: {
                                            id: 2,
                                            page_name: '',
                                            pageType: ''
                                        }
                                    }
                                ]
                            },
                            {
                                id: 312,
                                label: 'second order',
                                type: 'page_menu',
                                menus: [],
                                linked_page: {
                                    id: 2,
                                    page_name: '',
                                    pageType: ''
                                }
                            }
                        ]
                    }];
            }
        },
        created() {
            EventBus.$on('add-menu-item', this.addMenu);
            EventBus.$on('edit-menu-item', currentMenuItem => this.currentMenuItem = currentMenuItem);
            EventBus.$on('update-menu-item', menuItem => this.updateMenuItem(menuItem));
            this.initMenuStructure();
        }
    }
</script>
