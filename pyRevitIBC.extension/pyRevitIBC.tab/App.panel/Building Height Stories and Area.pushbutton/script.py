import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

from pyrevit import UI
from pyrevit import script
xamlFile = script.get_bundle_file('ui.xaml')

import wpf
from System import Windows

import IBC

__title__ = 'Chapter\n5\nHelper'

__doc__ = "This tool helps you quickly calculate your building's" \
          'maximum height, stories, and area.'

groups = ('A', 'B', 'E', 'F', 'H', 'I', 'M', 'R', 'S', 'U')

uses = ('1', '2', '3', '4', '5')

uses_AH = uses

uses_FS = ('1', '2')

uses_I = ('1 Condition 1', '1 Condition 2', '2', '3', '4')

uses_R = ('1', '2', '3', '4')

types = ('I-A', 'I-B', 'II-A', 'II-B', 'III-A', 'III-B', 'IV-HT', 'V-A', 'V-B')


class MyWindow(Windows.Window):
    def __init__(self):
        wpf.LoadComponent(self, xamlFile)

        self.setup_combobox()

    @property
    def selected_group(self):
        return self.group_cb.SelectedItem

    @property
    def selected_use(self):
        return self.use_cb.SelectedItem

    @property
    def selected_type(self):
        return self.type_cb.SelectedItem

    @property
    def ns_checked(self):
        return self.ns_chb.IsChecked

    @property
    def s_s1_checked(self):
        return self.s_s1_chb.IsChecked

    @property
    def s_sm_checked(self):
        return self.s_sm_chb.IsChecked

    @property
    def s13r_checked(self):
        return self.s13r_chb.IsChecked

    @property
    def s13d_checked(self):
        return self.s13d_chb.IsChecked

    def enable_s13r(self):
        self.s13r_chb.IsEnabled = True

    def disable_s13r(self):
        self.s13r_chb.IsChecked = False
        self.s13r_chb.IsEnabled = False

    def enable_s13d(self):
        self.s13d_chb.IsEnabled = True

    def disable_s13d(self):
        self.s13d_chb.IsChecked = False
        self.s13d_chb.IsEnabled = False

    def setup_combobox(self):
        self.group_cb.ItemsSource = groups
        self.use_cb.ItemsSource = uses
        self.type_cb.ItemsSource = types
        self.use_cb.IsEnabled = False

    def group_changed(self, sender, args):
        """Upon the group combobox being changed, updates use options accordingly"""
        group = self.selected_group

        # Update sprinklers if necessary (group changed to or from 'R')
        self.use_changed(None, None)

        self.use_cb.IsEnabled = True
        if group in 'A,H':
            self.use_cb.ItemsSource = uses_AH
        elif group in 'F,S':
            self.use_cb.ItemsSource = uses_FS
        elif group == 'I':
            self.use_cb.ItemsSource = uses_I
        elif group == 'R':
            self.use_cb.ItemsSource = uses_R
        else:
            self.use_cb.ItemsSource = None
            self.use_cb.IsEnabled = False

    def use_changed(self, sender, args):
        """Upon the use combobox being changed, updates sprinkler options for group 'R'"""
        group = self.selected_group

        if group != 'R':
            self.disable_s13d()
            self.disable_s13r()
        else:
            self.enable_s13r()

            if self.selected_use is not None and self.selected_use in '1,2':
                self.disable_s13d()
            else:
                self.enable_s13d()

    def compute(self, sender, args):
        group = self.group_cb.SelectedItem
        use = self.use_cb.SelectedItem
        type = self.type_cb.SelectedItem

        sprinkler = self.compute_sprinkler()

        if not group or not use or not type or not sprinkler:
            return

        height = IBC.allowable_height(group, use, sprinkler, type)
        stories = IBC.allowable_stories(group, use, sprinkler, type)
        area = IBC.allowable_area(group, use, sprinkler, type)

        if stories == 'NP' or area == 'NP':
            UI.TaskDialog.Show(
                "Results",
                "This combination is not permitted"
            )
        elif area == 'Unlimited':
            UI.TaskDialog.Show(
                "Results",
                """Max height: {height} Max stories: {stories} \n
                Unlimited area"""
            )
        elif sprinkler == 'S13R':
            UI.TaskDialog.Show(
                "Results",
                """Max height: {height} Max stories: {stories} \n
                Max area per story: {area} \n
                Max area total: {area} x N \n
                Where N = stories above grade plane, up to four""".format(height=height, stories=stories, area=area)
            )
        else:
            UI.TaskDialog.Show(
                "Results",
                """Max height: {height} Max stories: {stories} \n
                Max area per story: {area} \n
                Max area total: {area} x N \n
                Where N = stories above grade plane, up to three""".format(height=height, stories=stories, area=area)
            )

    def compute_sprinkler(self):
        """Return a string describing which sprinkler option is checked."""
        if self.ns_checked:
            return 'NS'
        elif self.s_s1_checked:
            return 'S1'
        elif self.s_sm_checked:
            return 'SM'
        elif self.s13r_checked:
            return 'S13R'
        elif self.s13d_checked:
            return 'S13D'
        else:
            return None


MyWindow().ShowDialog()
