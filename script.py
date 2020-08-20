import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

from pyrevit import forms
from pyrevit import revit
from pyrevit import UI
from pyrevit import script
xamlFile = script.get_bundle_file('ui.xaml')

from IBC import allowable_height, allowable_stories, allowable_area
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


class MakeIntroWindow(forms.WPFWindow):
    def __init__(self, xaml_file_name, rvt_elements=None):
        self._export_only = False

        forms.WPFWindow.__init__(self, xaml_file_name)

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
        self.uses_cb.IsEnabled = False

    def group_changed(self):
        """Upon the group combobox being changed, updates use options accordingly"""
        group = self.selected_group()

        self.use_changed()

        # Reset uses to prevent incompatible selections
        self.uses_cb.SelectedIndex = 0

        if group in 'A,H':
            self.uses_cb.ItemsSource = uses_AH
        elif group in 'F,S':
            self.uses_cb.ItemsSource = uses_FS
        elif group == 'I':
            self.uses_cb.ItemsSource = uses_I
        elif group == 'R':
            self.uses_cb.ItemsSource = uses_R
        else:
            self.uses_cb.IsEnabled = False

    def use_changed(self):
        """Upon the use combobox being changed, updates sprinkler options for group 'R'"""
        group = self.selected_group()

        if group != 'R':
            self.disable_s13d()
            self.disable_s13r()
        else:
            self.enable_s13r()

            if self.selected_use in '1,2':
                self.disable_s13d()
            else:
                self.enable_s13d()

    def compute(self, sender, args):
        group = self.group_cb.SelectedItem
        use = self.use_cb.SelectedItem
        type = self.type_cb.SelectedItem

        sprinkler = self.compute_sprinkler()

        height, stories, area = -1

        height = allowable_height(group, use, sprinkler, type)
        stories = allowable_stories(group, use, sprinkler, type)
        area = allowable_area(group, use, sprinkler, type)
        # Currently hard-coded to only use IBC (2018)
        height = IBC.allowable_height(group, use, sprinkler, type)
        stories = IBC.allowable_stories(group, use, sprinkler, type)
        area = IBC.allowable_area(group, use, sprinkler, type)

        result = "Height: " + str(height) + " Stories: " + str(stories) + " Area: " + str(area)

        # TODO: Decide on how to display results to user
        UI.TaskDialog.Show(
            "Results",
            "Results: {}".format(result)
        )

        # if isinstance(height, basestring) or isinstance(stories, basestring) or isinstance(area, basestring):


    def compute_sprinkler(self):
        """Return a string describing which sprinkler option is checked."""
        if self.ns_checked():
            return 'NS'
        elif self.s_s1_checked():
            return 'S1'
        elif self.s_sm_checked():
            return 'SM'
        elif self.s13r_checked():
            return 'S13R'
        elif self.s13d_checked():
            return 'S13D'

if __name__ == '__main__':
    MakeIntroWindow('MakePatternWindow.xaml').show(modal=True)